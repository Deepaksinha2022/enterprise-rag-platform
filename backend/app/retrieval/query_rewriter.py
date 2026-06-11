def rewrite_query(
    query
):

    query = query.lower()

    replacements = {

        "vacation": "annual leave",

        "vacation days": "annual leave",

        "work from home": "remote work",

        "health insurance": "employee benefits",

        "medical leave": "sick leave"

    }

    for old, new in replacements.items():

        query = query.replace(
            old,
            new
        )

    return query