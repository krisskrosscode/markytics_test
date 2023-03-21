or data in final_df.to_dict('r'):
#     """ Updating lead list """
#     field_5_string = f"।।आपके पास।।।।,"  ## stores all counts as formatted string

#     pending_count = data['Pending_Count']
#     field_5_string += ((str(pending_count) + pending_count_hindi_text + '। जिनमें से ,') if pending_count != 0 else '')

#     collection_count = data['collection_count']
#     field_5_string += ((str(collection_count) + collection_count_hindi_text) if collection_count != 0 else '')

#     proposal_count = data['proposal_count']
#     field_5_string += ((str(proposal_count) + proposal_count_hindi_text) if proposal_count != 0 else '')

#     retention_count = data['retention_count']
#     field_5_string += ((str(retention_count) + retention_count_hindi_text) if retention_count != 0 else '')


#     wrong_number_count = data['wrong_number_count']
#     field_5_string += ((str(wrong_number_count) + wrong_number_count_hindi_text) if wrong_number_count != 0 else '')



#     # ।।।।   ,,..सोनाटा फाइनेंस सारथि एप्लीकेशन में आपका स्वागत है ! \\
#     #     प्रिय {data['UserName']} जी, आज आपको निम्न कार्य सूचि प्राथमिकता से सम्पूर्ण करनी है! \\
#     #     आपके पास।।।। 
#     # print(data['CallingNumber'], "//////////////////")
#     if ('+91'+ data['CallingNumber']) in leadlist.keys():
#         # data['status'] = '1'
#         # update_lead(leadlist['+91' + '9162841833'])
#         # print(data['CallingNumber'])
#         lead_id = leadlist['+91' + data['CallingNumber']]  #leadlist['+91' + '9162841833']
#         url = f"https://api-smartflo.tatateleservices.com/v1/broadcast/lead/{lead_id}" ## update lead api call

#         headers = {
#             "accept": "application/json",
#             "Authorization": auth_token,
#             "content-type": "application/json"
#         }
#         payload = {
#             'dial_status' : '1',
#             'field_1': data['UserName'],
#             'field_5': field_5_string
#         }
#         # response = requests.put(url, headers=headers, json= payload)
#         # print(response.text)
 
#     else: 
#         url = f"https://api-smartflo.tatateleservices.com/v1/broadcast/lead/{MORNING_LEAD_LIST_ID}"

#         payload = json.dumps({
#         "field_0": data['CallingNumber'],
#         # "field_0": '9162841833',
#         "field_1": data['UserName'],
#         "field_5": field_5_string,
#         # "field_6": (str(data['collection_count']) + collection_count_hindi_text) if data['collection_count'] != 0 else '',
#         # "field_7": (str(data['proposal_count']) + proposal_count_hindi_text) if data['proposal_count'] != 0 else '',
#         # "field_8": (str(data['retention_count']) + retention_count_hindi_text) if data['retention_count'] != 0 else '',
#         # "field_9": (str(data['wrong_number_count']) + wrong_number_count_hindi_text if data['wrong_number_count'] != 0 else '' ),
#         })
#         headers = {
#         'Accept': 'application/json',
#         'Authorization': auth_token,
#         'Content-Type': 'application/json'
#         }

#         # response = requests.request("POST", url, headers=headers, data=payload)

#         # print(response.text)
