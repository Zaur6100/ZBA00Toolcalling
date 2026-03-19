validation_examples = [
    #1. get_weather
    {
        "messages": [
            {"role": "user", "content": "What's the temperature in Odense right now?"},
            {
                "role": "assistant",
                "tool_calls": [
                    {
                        "name": "get_weather",
                        "arguments": {"location": "Odense", "unit": "celsius"},
                    }
                ],
            },
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Is it going to rain in Copenhagen today?"},
            {
                "role": "assistant",
                "tool_calls": [
                    {
                        "name": "get_weather",
                        "arguments": {"location": "Copenhagen", "unit": "celsius"},
                    }
                ],
            },
        ]
    },

    #2. correct_grammar
    {
        "messages": [
            {"role": "user", "content": "Fix this sentence: Me and him goes to the store yesterday."},
            {
                "role": "assistant",
                "tool_calls": [
                    {
                        "name": "correct_grammar",
                        "arguments": {"text": "Me and him goes to the store yesterday."},
                    }
                ],
            },
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Can you correct this: Their going too the park and they dont care about there homework."},
            {
                "role": "assistant",
                "tool_calls": [
                    {
                        "name": "correct_grammar",
                        "arguments": {"text": "Their going too the park and they dont care about there homework."},
                    }
                ],
            },
        ]
    },

    #3. generate_image
    {
        "messages": [
            {"role": "user", "content": "Create a watercolor painting of a sunset in denmark"},
            {
                "role": "assistant",
                "tool_calls": [
                    {
                        "name": "generate_image",
                        "arguments": {"prompt": "sunset in denmark", "style": "watercolor"},
                    }
                ],
            },
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Generate a realistic photo of an AI-student working on his bachelor project."},
            {
                "role": "assistant",
                "tool_calls": [
                    {
                        "name": "generate_image",
                        "arguments": {"prompt": "AI-student working on his bachelor project", "style": "realistic"},
                    }
                ],
            },
        ]
    },

    #4. text_to_speech
    {
        "messages": [
            {"role": "user", "content": "Read this out loud: The validation examples should be ready on thursday"},
            {
                "role": "assistant",
                "tool_calls": [
                    {
                        "name": "text_to_speech",
                        "arguments": {"text": "The validation examples should be ready on thursday", "voice": "neutral"},
                    }
                ],
            },
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Convert to speech in a female voice: Welcome to our presentation on machine learning."},
            {
                "role": "assistant",
                "tool_calls": [
                    {
                        "name": "text_to_speech",
                        "arguments": {"text": "Welcome to our presentation on machine learning.", "voice": "female"},
                    }
                ],
            },
        ]
    },

    #5. search_web
    {
        "messages": [
            {"role": "user", "content": "Look up the latest news about Trump taking over greenland."},
            {
                "role": "assistant",
                "tool_calls": [
                    {
                        "name": "search_web",
                        "arguments": {"query": "latest news about Trump taking over greenland"},
                    }
                ],
            },
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Search for the current world population in 2026."},
            {
                "role": "assistant",
                "tool_calls": [
                    {
                        "name": "search_web",
                        "arguments": {"query": "current world population 2026"},
                    }
                ],
            },
        ]
    },
]