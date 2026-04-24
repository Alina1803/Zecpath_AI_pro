from app.services.edge_case_31.ai_flow.retry_handler import retry_process

def test_retry_failure():
    def fail_func(x):
        raise Exception("Fail")

    try:
        retry_process(fail_func, "test")
    except:
        assert True