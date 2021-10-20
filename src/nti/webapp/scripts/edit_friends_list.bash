#!/bin/bash
counter=1
group_size=20
while [ $counter -le 99 ]
do
  new_friends_list="stress.tester$((counter + group_size - counter % group_size))"
  echo '{

  "Creator": '"\"stress.tester$counter\""', "CreatedTime": 1632344251.669365,
                      "Last Modified": 1632344251.670834,
                      "NTIID": '"\"tag:nextthought.com,2011-10:stress.tester$counter-MeetingRoom:Group-mycontacts_stress.tester$counter\""',
                      "MimeType": "application/vnd.nextthought.friendslist",
                      "OID": '"\"tag:nextthought.com,2011-10:stress.tester$counter-OID-0x29c418a4:5573657273:hEMRCH4cfK\""',
                      "Links": [{"hre": '"\"/dataserver2/counters/stress.tester$counter/FriendsLists/mycontacts-stress.tester$counter\""',
                                 "ntiid": '"\"tag:nextthought.com,2011-10:stress.tester$counter-MeetingRoom:Group-mycontacts_stress.tester$counter\""',
                                 "rel": "edit"}],
                      "hre": '"\"/dataserver2/counters/stress.tester$counter/FriendsLists/mycontacts-stress.tester$counter\""',
                      "alias": "My Contacts", "avatarURL": "", "blurredAvatarURL": "",
                      "ID": '"\"mycontacts-stress.tester$counter\""', "realname": '"\"mycontacts-stress.tester$counter\""',
                      "countername": '"\"mycontacts-stress.tester$counter\""', "friends": ['"\"$new_friends_list\""'], "params": "[]"


  }' | http --verify=false --verbose -a stress.tester$counter:temp001 PUT https://alpha.nextthought.com/dataserver2/users/stress.tester$counter/FriendsLists/mycontacts-stress.tester$counter
    echo "stress.tester$counter is now following $new_friends_list"
    ((counter++))
done