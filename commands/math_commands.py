async def evaluate_math_expression(command_data):
    expression = command_data.get("expression")
    try:
        result = eval(expression)  # توجه: eval می‌تواند خطرناک باشد!
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}
