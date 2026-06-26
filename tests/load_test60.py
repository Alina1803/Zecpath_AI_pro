import random


def simulate_load(n=1000):

    results = []

    for _ in range(n):

        response = random.uniform(
            0.5,
            1.5,
        )

        results.append(response)

    avg = sum(results) / len(results)

    return {
        "avg_response": round(
            avg,
            2,
        ),
        "max_response": max(results),
    }


if __name__ == "__main__":

    print(simulate_load())
