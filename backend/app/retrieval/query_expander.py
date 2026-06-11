def expand_query(
    query
):

    expansions = {

        "annual leave": [

            "paid leave",

            "leave entitlement"
        ],

        "sick leave": [

            "medical leave",

            "health leave"
        ],

        "employee benefits": [

            "health insurance",

            "benefits package"
        ],

        "remote work": [

            "work from home",

            "wfh"
        ]

    }

    expanded_queries = [

        query
    ]

    for key, values in expansions.items():

        if key in query.lower():

            expanded_queries.extend(
                values
            )

    return expanded_queries