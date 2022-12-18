from pytest_voluptuous import S
from requests import Response
from schemas.reqres import list_users_schema, create_user_schema, update_user_schema, login_unsucc_schema


def test_get_list_users(reqres_session):

    page_number = 2

    result: Response = reqres_session.get(
        url='/api/users',
        params={'page': page_number}
    )

    assert result.status_code == 200
    assert result.json()['page'] == page_number
    assert result.json() == S(list_users_schema)


def test_create_user(reqres_session):
    name = 'Evgen'
    job = 'AQA'

    result: Response = reqres_session.post(
        url='/api/users',
        json=
        {
            "name": name,
            "job": job
        }
    )

    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert result.json() == S(create_user_schema)


def test_update_patch_user(reqres_session):
    name = 'Evgen'
    job = 'AQA'
    id = 2

    result: Response = reqres_session.patch(
        url=f'/api/users/{id}',
        json=
        {
            "name": name,
            "job": job
        }
    )

    assert result.status_code == 200
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert result.json() == S(update_user_schema)


def test_delete_user(reqres_session):
    id = 2
    result: Response = reqres_session.delete(f'/api/users/{id}')
    assert result.status_code == 204


def test_login_unsuccessful(reqres_session):
    email = 'peter@klaven'

    result: Response = reqres_session.post(
        url='/api/login',
        json={
            "email": email
        }
    )

    assert result.status_code == 400
    assert result.json() == S(login_unsucc_schema)
    assert result.json()['error'] == 'Missing password'
