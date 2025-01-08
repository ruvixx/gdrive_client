from gdrive.utils.service import get_service


def list_files(fields=None, page_size=20, q=None, max_results=100):
    """
    Generator function that yields all files matching the query criteria.
    Handles pagination automatically unless nextPageToken is not provided 
    in fields.

    TODO: Add limit support
    TODO: Add support for other fields
    """
    service = get_service("drive", "v3")
    page_token = None
    fields = "nextPageToken, files(id, name)" if fields is None else fields
    files_count = 0
    request = (
        service.files()
        .list(
            pageSize=page_size,
            fields=fields,
            pageToken=page_token,
            q=q,
        )
    )
    while request is not None:
        results = request.execute()

        files = results.get("files", [])
        yield from files

        request = service.files().list_next(request, results)

        # page_token = results.get("nextPageToken")
        # if not page_token:
        #     break
