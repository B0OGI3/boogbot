import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.call_function import available_functions, call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key == None:
    raise RuntimeError("Invalid API Key")


client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

for i in range(20):

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
            ),
        )

        for candidate in response.candidates:
            messages.append(candidate.content)

        if response.usage_metadata == None:
            raise RuntimeError("No response metadata")

        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        if response.function_calls:
            function_responses = []

            for call in response.function_calls:
                function_call_result = call_function(call, verbose=args.verbose)
                part = function_call_result.parts[0]
                if not getattr(part, "function_response", None):
                    raise RuntimeError("Function call returned no function_response")

                function_responses.append(part)

                if args.verbose:
                    print(f"-> {part.function_response.response}")
                
            messages.append(types.Content(role="user", parts=function_responses))

        elif not response.function_calls and response.text:
            print(response.text)
            break
        else:
            print(response.text)
        


    except Exception as error:
        print(f"Error: {error}")

 
