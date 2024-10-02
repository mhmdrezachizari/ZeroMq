import sympy as sp

async def evaluate_math_expression(command_data):
    expression = command_data.get("expression")
    try:
        result = sp.sympify(expression)
        return {"result": int(result)}
    except sp.SympifyError:
        return {"error": "Invalid mathematical expression"}
    except Exception as e:
        return {"error": str(e)}
