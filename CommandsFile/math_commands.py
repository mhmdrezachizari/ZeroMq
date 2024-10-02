import sympy as Math

async def evaluate_math_expression(command_data):
    expression = command_data.get("expression")
    try:
        result = Math.sympify(expression)
        return {"result": int(result)}
    except Math.SympifyError:
        return {"error": "mmmm i think you have wrong expression"}
    except Exception as error:
        return {"error": str(error)}
