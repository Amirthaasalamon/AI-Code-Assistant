def read_uploaded_files(uploaded_files):
    files_data = []

    for file in uploaded_files:
        try:
            content = file.read().decode("utf-8")
        except:
            content = "Unable to read file"

        files_data.append({
            "name": file.name,
            "content": content
        })

    return files_data