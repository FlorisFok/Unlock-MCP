import asyncio

from agents import Agent, Runner
from agents.mcp import MCPServerStdio
from agents.model_settings import ModelSettings
from agents.run import RunConfig


async def main() -> None:
    # Connect to the MCP servers via stdio
    async with MCPServerStdio(
        name="DynamicCalculatorTools",
        params={
            "command": "python",
            "args": ["server.py"],
        },
    ) as calculator_server, MCPServerStdio(
        name="StringOperationsTools",
        params={
            "command": "python",
            "args": ["server2.py"],
        },
    ) as string_server:
        agent = Agent(
            name="Assistant",
            instructions="Access the tools to answer the questions.",
            mcp_servers=[calculator_server, string_server],
            model_settings=ModelSettings(tool_choice="required"),
        )

        result = await Runner.run(
            agent,
            "Please use the tools to calculate: 456789 + 4567890",
            run_config=RunConfig(tracing_disabled=True),
        )
        print(result.final_output)

        # Show the tool calls made
        print("\nRaw responses:")
        for item in result.raw_responses:
            print(item)
            print("--------------------------------")


asyncio.run(main())



# Raw responses:
### # Raw responses:
# ModelResponse(output=[ResponseFunctionToolCall(arguments='{}', call_id='call_xhhya1BlcsjvGRz1rHnKbmPE', name='access_calculator_tools', type='function_call', id='fc_0fb562efd77d58e70169675871e99081989f9f2ee2ddbc7396', status='completed')], usage=Usage(requests=1, input_tokens=83, input_tokens_details=InputTokensDetails(cached_tokens=0), output_tokens=13, output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=96), response_id='resp_0fb562efd77d58e7016967587196188198a0c27551ffbab751')
# --------------------------------
# ModelResponse(output=[ResponseFunctionToolCall(arguments='{"a":456789,"b":4567890}', call_id='call_9bxjigMgMZiJbwSs8CDsR1bE', name='add_numbers', type='function_call', id='fc_0fb562efd77d58e70169675872f5108198a2f69a0c47e44acd', status='completed')], usage=Usage(requests=1, input_tokens=603, input_tokens_details=InputTokensDetails(cached_tokens=0), output_tokens=22, output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=625), response_id='resp_0fb562efd77d58e7016967587227e08198a94687e96b023595')
# --------------------------------
# ModelResponse(output=[ResponseOutputMessage(id='msg_0fb562efd77d58e7016967587379948198a2a7c04e5e867582', content=[ResponseOutputText(annotations=[], text='The result of \\(456789 + 4567890\\) is 5024679.', type='output_text', logprobs=[])], role='assistant', status='completed', type='message')], usage=Usage(requests=1, input_tokens=649, input_tokens_details=InputTokensDetails(cached_tokens=0), output_tokens=21, output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=670), response_id='resp_0fb562efd77d58e7016967587337e08198a4e945bdf3fc34d2')
# --------------------------------

### # ALLLL
# Raw responses:
# ModelResponse(output=[ResponseFunctionToolCall(arguments='{"a":456789,"b":4567890}', call_id='call_DUrOZA5tYhmZLtEK4vr8qEmc', name='add_numbers', type='function_call', id='fc_01e56e754fd26b91016967583c5f9881998b298849f9e44490', status='completed')], usage=Usage(requests=1, input_tokens=1232, input_tokens_details=InputTokensDetails(cached_tokens=0), output_tokens=22, output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=1254), response_id='resp_01e56e754fd26b91016967583b9e84819980fc018f6655e39d')
# --------------------------------
# ModelResponse(output=[ResponseOutputMessage(id='msg_01e56e754fd26b91016967583da810819990b0d5e5b11c87e7', content=[ResponseOutputText(annotations=[], text='The result of 456789 + 4567890 is 5024679.', type='output_text', logprobs=[])], role='assistant', status='completed', type='message')], usage=Usage(requests=1, input_tokens=1278, input_tokens_details=InputTokensDetails(cached_tokens=1152), output_tokens=19, output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=1297), response_id='resp_01e56e754fd26b91016967583d23008199a51d905781aa8155')
# --------------------------------