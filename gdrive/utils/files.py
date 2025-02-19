from gdrive.utils.service import get_service


def list_files(fields=None, page_size=20, q=None, max_results=100, folder_id=None):
    """
    Generator function that yields all files matching the query criteria.
    Handles pagination automatically unless nextPageToken is not provided
    in fields.

    Args:
        fields (str, optional): Fields to include in response. Defaults to "nextPageToken, files(id, name)".
        page_size (int, optional): Number of files per page. Defaults to 20.
        q (str, optional): Search query. Defaults to None.
        max_results (int, optional): Maximum number of results to return. Defaults to 100.
        folder_id (str, optional): ID of folder to list files from. Defaults to None.

    TODO: Add limit support
    TODO: Add support for other fields
    """
    service = get_service("drive", "v3")
    page_token = None
    fields = "nextPageToken, files(id, name)" if fields is None else fields
    files_count = 0

    # Add folder filter to query if folder_id provided
    if folder_id:
        folder_query = f"'{folder_id}' in parents"
        q = folder_query if q is None else f"{q} and {folder_query}"

    request = service.files().list(
        pageSize=page_size,
        fields=fields,
        pageToken=page_token,
        q=q,
    )
    while request is not None:
        results = request.execute()

        files = results.get("files", [])
        yield from files

        request = service.files().list_next(request, results)

        # page_token = results.get("nextPageToken")
        # if not page_token:
        #     break
