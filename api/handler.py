import random

def handler(request, response):
    try:
        success = random.choices(['fail', 'pass'], weights=[40, 60])[0]
        if success == 'fail':
            result = "Chaos Scroll has failed. No changes made, an upgrade slot has been consumed."
        else:
            stat_change = random.randint(-5, 5)
            result = f"Chaos Scroll has passed and your item got a {stat_change:+d} stats !"

        return response.json({"result": result})
    except Exception as e:
        return response.json({"error": str(e)}, status=500)
