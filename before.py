# BEFORE: messy + bug
# Bug: it wrongly skips "pending" entries due to a bad condition.

def process(records):
    total = 0
    paid = 0
    pending = 0
    failed = 0

    for r in records:
        # r example: {"amount": 10.0, "status": "pending"}
        if r["status"] == "paid":
            paid += 1
            total += r["amount"]
        elif r["status"] == "pending":
            # BUG: should count pending, but mistakenly continues and does nothing
            if r["status"] != "pending":
                pending += 1
            continue
        elif r["status"] == "failed":
            failed += 1
        else:
            pass

    return {"total": total, "paid": paid, "pending": pending, "failed": failed}


if __name__ == "__main__":
    sample = [
        {"amount": 100.0, "status": "paid"},
        {"amount": 50.0, "status": "pending"},
        {"amount": 10.0, "status": "failed"},
    ]
    print(process(sample))
