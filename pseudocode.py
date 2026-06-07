function process_complaint(complaint_text, user_details):

    complaint_id = generate_unique_id()

    issues = extract_issues(complaint_text)

    category = classify_complaint(issues)

    priority = assign_priority(issues, category)

    departments = map_to_departments(category)

    for dept in departments:
        sub_complaint = {
            "complaint_id": complaint_id,
            "department": dept,
            "issues": issues,
            "priority": priority,
            "status": "open"
        }
        save_to_db(sub_complaint)

    send_notification(user_details, complaint_id)

    return {
        "complaint_id": complaint_id,
        "departments": departments,
        "priority": priority,
        "status": "submitted"
    }