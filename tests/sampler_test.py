import json
    assert sample.FAIL_TO_PASS == json.dumps(["test_test_command"])
    mock_call_llm_api.set_streamed_values(
        [
            dedent(
                """\
        @@end"""
            )
        ]

    session = Session(cwd=Path.cwd(), paths=[Path("multifile_calculator/calculator.py")])
    assert sample.FAIL_TO_PASS == json.dumps(["test_test_command"])
    assert sample.version == "0.3.0"
        "I will add a new sha1 function to the `utils.py` file.\n\nSteps:\n1. Add the sha1 function to `utils.py`."
    "FAIL_TO_PASS": "",
    "version": "0.3.0",
@pytest.mark.ragdaemon
async def test_sample_eval(temp_testbed, mock_call_llm_api):
    mock_call_llm_api.set_streamed_values(
        [
            dedent(
                f"""\
        1. Add the `sha1` function to `mentat/utils.py`.{edit_message}"""
            )
        ]
    )
    (temp_testbed / "scripts" / "graph_class.py").rename(temp_testbed / "scripts" / "graph.py")
async def test_sampler_integration(temp_testbed, mock_session_context, mock_call_llm_api):
        ("operations.py" in str(f.file_path) and "return a - b" not in str(f.replacements))
    mock_call_llm_api.set_streamed_values([f"I will make the following edits. {llm_response}"])
    await client.call_mentat_auto_accept(
        dedent(
            """\
        """
        )
    )
    await client.call_mentat("")
    mock_call_llm_api.set_streamed_values([f"I will make the following edits. {llm_response}"])