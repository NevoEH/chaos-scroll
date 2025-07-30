import random
import json

def handler(request):
    try:
        success = random.choices(['fail', 'pass'], weights=[40, 60])[0]
        if success == 'fail':
            result = "Chaos Scroll has failed. No changes made, an upgrade slot has been consumed."
        else:
            stat_change = random.randint(-5, 5)
            result = f"Chaos Scroll has passed and your item got a {stat_change:+d} stats !"

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"result": result})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)})
        }
