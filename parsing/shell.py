import CodeSimple

while True:
    text = input('CodeSimple > ')
    if text.lower() == 'exit':
        break

    result, error = CodeSimple.run(text)

    if error:
        print(error.as_string())
    else:
        print(result)
