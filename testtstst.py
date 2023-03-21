import requests


user_number = '8335076174'
task_id = '12'
creator_name =  'abhijith'
category = 'category'
creator_role =  'asdasd'
customer_name=  'abhijith'
customer_code =  'abhijith'
priority=  'abhijith'
promise_time=  'abhijith'
promise_amount = 'abhijith'
payment_collection_location=  'abhijith'
task_deadline = 'abhijith'

url = "https://media.smsgupshup.com/GatewayAPI/rest"
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
payload =f'userid=2000209909&password=z24gzBUA&method=SendMessage&auth_scheme=plain&v=1.1&send_to={user_number}&msg=%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF%20%E0%A4%86%E0%A4%88%E0%A4%A1%E0%A5%80%3A%20{task_id}%0A%E0%A4%86%E0%A4%AA%E0%A4%95%E0%A5%8B%20%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%80%E0%A4%AE%E0%A4%BE%E0%A4%A8%20{creator_name}({creator_role})%20%E0%A4%B8%E0%A5%87%20%E0%A4%8F%E0%A4%95%20%E0%A4%A8%E0%A4%AF%E0%A4%BE%20%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF%20%E0%A4%B8%E0%A5%8C%E0%A4%82%E0%A4%AA%E0%A4%BE%20%E0%A4%97%E0%A4%AF%E0%A4%BE%20%E0%A4%B9%E0%A5%88%E0%A5%A4%0A%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF%20%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%87%E0%A4%A3%E0%A5%80%20{category}%20%E0%A4%B9%E0%A5%88%E0%A5%A4%0A%E0%A4%89%E0%A4%AA%E0%A4%AD%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%BE%20%E0%A4%B5%E0%A4%BF%E0%A4%B5%E0%A4%B0%E0%A4%A3%3A%20{customer_name}({customer_code})%0A%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF%20%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%A5%E0%A4%AE%E0%A4%BF%E0%A4%95%E0%A4%A4%E0%A4%BE%20{priority}%20%E0%A4%B9%E0%A5%88%E0%A5%A4%0A%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF%20%E0%A4%95%E0%A5%80%20%E0%A4%B8%E0%A4%AE%E0%A4%AF%20%E0%A4%B8%E0%A5%80%E0%A4%AE%E0%A4%BE%20%E0%A4%B9%E0%A5%88%20{task_deadline}.%0A%E0%A4%85%E0%A4%A7%E0%A4%BF%E0%A4%95%20%E0%A4%9C%E0%A4%BE%E0%A4%A8%E0%A4%A8%E0%A5%87%20%E0%A4%95%E0%A5%87%20%E0%A4%B2%E0%A4%BF%E0%A4%8F%20%E0%A4%A8%E0%A5%80%E0%A4%9A%E0%A5%87%20%E0%A4%A6%E0%A4%BF%E0%A4%8F%20%E0%A4%97%E0%A4%8F%20%E0%A4%B2%E0%A4%BF%E0%A4%82%E0%A4%95%20%E0%A4%95%E0%A4%BE%20%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%AF%E0%A5%8B%E0%A4%97%20%E0%A4%95%E0%A4%B0%E0%A5%87%E0%A4%82%E0%A5%A4&msg_type=hsm&isHSM=true&isTemplate=true&data_encoding=Text&format=json&header=%E0%A4%86%E0%A4%AA%E0%A4%95%E0%A5%87%20%E0%A4%AA%E0%A4%BE%E0%A4%B8%20%E0%A4%8F%E0%A4%95%20%E0%A4%A8%E0%A4%AF%E0%A4%BE%20%E0%A4%95%E0%A4%BE%E0%A4%B0%E0%A5%8D%E0%A4%AF%20%E0%A4%B9%E0%A5%88&buttonUrlParam={task_id}'
response = requests.request("POST", url, headers=headers, data=payload)