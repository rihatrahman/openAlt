def wikipediaIngest(uniqueEvent, cursor, connection):
    for key, value in uniqueEvent.items():
        if key == "license":
            t_license = value
        elif (key == "terms"):
            t_terms = value
        elif (key == "updated_reason"):
            t_updatedReason = value
        elif (key == "obj_id"):
            t_obj_id = value
        elif (key == "source_token"):
            t_source_token = value
        elif (key == "occurred_at"):
            t_occurred_at = value
        elif (key == "subj_id"):
            t_subj_id = value
        elif (key == "id"):
            t_id = value
        elif (key == "evidence_record"):
            t_evidence_record = value
        elif (key == "action"):
            t_action = value
        elif (key == 'subj'):
            subj_fields = uniqueEvent.get("subj")
            for key, value in subj_fields.items():
                if(key == 'pid'):
                    t_pid = value
                elif(key == 'url'):
                    t_url = value
                elif(key == 'title'):
                    t_title = value
                elif(key == 'api-url'):
                    t_api_url = value
        elif (key == 'source_id'):
            t_source_id = value
        elif (key == 'obj'):
            obj_fields = uniqueEvent.get('obj')
            for key, value in obj_fields.items():
                if(key == 'pid'):
                    t_pid = value
                elif(key == 'url'):
                    t_url = value
        elif (key == 'timestamp'):
            t_timestamp = value
        elif (key == "updated_date"):
            t_updated_date = value
        elif (key == 'relation_type_id'):
            t_relation_type_id = value
    # cursor.execute()

    add_event = (
        "INSERT IGNORE INTO WikipediaEvent " "(license, termsOfUse, updatedDate, updatedReason, objectID, sourceToken, occuredAt, subjectID, eventID, evidenceRecord, eventAction, subjectPID, subjectTitle, subjectURL, subjectAPIURL, sourceID, objectPID, objectURL, timeObserved, relationType) " "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    # Values to insert into wikipediaevent table  - LEAVE OUT THE OBJECT ID
    data_event = (
    t_license, t_terms, t_updated_date, t_updatedReason, t_obj_id, t_source_token, t_occurred_at, t_subj_id, t_id,
    t_evidence_record, t_action, t_pid, t_title, t_url, t_api_url, t_source_id, t_pid, t_url, t_timestamp, t_relation_type_id)

    add_to_main = ("INSERT IGNORE INTO main (objectID) VALUES (\'" + t_obj_id + "\');")

    cursor.execute(add_to_main)
    cursor.execute(add_event, data_event)  # add information to wikipediaevent table
    connection.commit()