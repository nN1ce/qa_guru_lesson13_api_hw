from voluptuous import Schema, PREVENT_EXTRA, All, Length, Any

list_user_data_schema = Schema(
    {
        "id": int,
        "email": str,
        "first_name": str,
        "last_name": str,
        "avatar": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

list_user_support_schema = Schema(
    {
        "url": str,
        "text": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

list_users_schema = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": All([list_user_data_schema], Length(min=1)),
        "support": list_user_support_schema
    },
    required=True,
    extra=PREVENT_EXTRA
)

create_user_schema = Schema(
    {
        "name": str,
        "job": Any(str, None),
        "id": str,
        "createdAt": str,
    },
    required=True,
    extra=PREVENT_EXTRA
)

update_user_schema = Schema(
    {
        "name": str,
        "job": Any(str, None),
        "updatedAt": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

login_unsucc_schema = Schema(
    {
        "error": str
    },
    required=True,
    extra=PREVENT_EXTRA
)
