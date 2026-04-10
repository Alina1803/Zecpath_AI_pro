from concurrent.futures import ThreadPoolExecutor

def process_single_resume(resume_path):
    from parsers.resume_parser import parse_resume
    return parse_resume(resume_path)


def process_resumes_in_batch(resume_paths, max_workers=4):
    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_single_resume, path) for path in resume_paths]

        for future in futures:
            try:
                results.append(future.result())
            except Exception as e:
                print(f"Error processing resume: {e}")

    return results