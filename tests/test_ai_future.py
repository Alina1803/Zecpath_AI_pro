from app.services.future_58.future_pipeline import (
    FuturePipeline
)


def test_pipeline():

    result=(

        FuturePipeline()

        .process_candidate(

            "AI001",

            {

                "communication":60,

                "confidence":55,

            }

        )

    )

    assert (

        result[
            "status"
        ]

        ==

        "success"

    )