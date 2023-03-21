##cpoied from rdc

if queue_running_inst.stage == '1.1':
                    # try:    
                    date = json_data['text']
                    queue_running_inst.field_11 = date
                    queue_running_inst.save()
                    from datetime import date as dt
                    date = dt(int('20' + date[4:6]), int(date[2:4]), int(date[0:2]))
                    if date < date.today():
                        print()
                    issues_id = queue_running_inst.issue_id
                    user1 = os.environ['PAYMEE_SONTATA_DB_USER']
                    password = os.environ['PAYMEE_SONTATA_DB_PASSWORD']
                    db = "Sonata_Connect_Test"
                    server = "172.17.130.216"
                    engine = create_engine(f"mssql+pyodbc://{user1}:{password}@{server}/{db}?driver=ODBC+Driver+17+for+SQL+Server")
                    sql_query = f""" SELECT * from Sonata_Connect.dbo.CallingIssues ci  where id = {issues_id} """
                    dg=pd.read_sql_query(sql_query,engine)
                    # dg = pd.DataFrame(CallingIssues.objects.filter(id=issues_id).values())
                    amt = int(dg['promise_amount'].iloc[0])
                    customer_name = dg['customer_name'].iloc[0]
                    task_idd = dg['bro_taskid'][0]
                    
                    user1 = os.environ['PAYMEE_SONTATA_DB_USER']
                    password = os.environ['PAYMEE_SONTATA_DB_PASSWORD']
                    db = "Sonata_Connect"
                    server = "172.17.130.216"
                    engine = create_engine(f"mssql+pyodbc://{user1}:{password}@{server}/{db}?driver=ODBC+Driver+17+for+SQL+Server")
                    sql_query = f""" SELECT * from Sonata_Connect.dbo.accounts_task_details where task_id = {task_idd} """
                    dgg=pd.read_sql_query(sql_query,engine)
                    desc_p = str(dgg['task_description'][0]).split(' ')
                    cust_code = desc_p[3][:-1]
                    remain_txt = ' '.join([str(elem) for elem in desc_p[14:]])
                    try:
                        if queue_running_inst.field_12 is not None:
                            collected = queue_running_inst.field_12
                            amt = amt - collected
                            full_desc = f'Customer (Customer id: {cust_code}) will pay an amount of Rs.{amt} on {date} 10:30 by {remain_txt}'
                            task_details.objects.filter(task_id=task_idd).update(task_description=full_desc)
                            CallingIssues.objects.filter(id=issues_id).update(promise_date=date,promise_amount=amt)
                        url = f"https://media.smsgupshup.com/GatewayAPI/rest?userid=2000209909&password=z24gzBUA&send_to={user_number}&v=1.1&format=json&msg_type=TEXT&method=SENDMESSAGE&msg=%E0%A4%95%E0%A5%83%E0%A4%AA%E0%A4%AF%E0%A4%BE+{str(date)}+%E0%A4%95%E0%A5%8B+%E0%A4%97%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%B9%E0%A4%95+{str(customer_name)}+%E0%A4%B8%E0%A5%87+{str(amt)}+%E0%A4%B0%E0%A5%81%E0%A4%AA%E0%A4%AF%E0%A5%87+%E0%A4%95%E0%A5%80+%E0%A4%AC%E0%A4%95%E0%A4%BE%E0%A4%AF%E0%A4%BE+%E0%A4%B0%E0%A4%BE%E0%A4%B6%E0%A4%BF+%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%AA%E0%A5%8D%E0%A4%A4+%E0%A4%95%E0%A4%B0%E0%A5%87%E0%A4%82&isTemplate=true&header=%E0%A4%A7%E0%A4%A8%E0%A5%8D%E0%A4%AF%E0%A4%B5%E0%A4%BE%E0%A4%A6"
                        payload={}
                        headers = {}
                        response = requests.request("GET", url, headers=headers, data=payload)
                        queue_running_inst.status = 'complete'
                        queue_running_inst.save()
                    except:
                        pass