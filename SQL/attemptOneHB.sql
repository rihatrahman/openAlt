/*
{
    "events": 
[
    {
      "license": "https://creativecommons.org/publicdomain/zero/1.0/",
      "terms": "https://doi.org/10.13003/CED-terms-of-use",
      "updated_reason": "https://evidence.eventdata.crossref.org/announcements/2018-04-26T00-00-00Z-ED-16.json",
      "updated": "edited",
      "obj_id": "https://doi.org/10.1098/rspb.2016.0792",
      "source_token": "45a1ef76-4f43-4cdc-9ba8-5a6ad01cc231",
      "occurred_at": "2017-02-17T09:17:34Z",
      "subj_id": "http://twitter.com/PaulKiem/statuses/832519346811310080",
      "id": "90dd1736-e4cc-4955-a9b4-6f5e18421348",
      "evidence_record": "https://evidence.eventdata.crossref.org/evidence/20170217f49152d6-b592-4320-a927-ee514d41600a",
      "action": "add",
      "subj": {
        "pid": "http://twitter.com/PaulKiem/statuses/832519346811310080",
        "title": "Tweet 832519346811310080",
        "issued": "2017-02-17T09:17:34.000Z",
        "author": {
          "url": "http://www.twitter.com/PaulKiem"
        },
        "original-tweet-url": "http://twitter.com/ScholarsLeague/statuses/832196260924841989",
        "original-tweet-author": "http://www.twitter.com/ScholarsLeague",
        "alternative-id": "832519346811310080"
      },
      "source_id": "twitter",
      "obj": {
        "pid": "https://doi.org/10.1098/rspb.2016.0792",
        "url": "https://doi.org/10.1098/rspb.2016.0792"
      },
      "timestamp": "2017-02-17T12:20:02Z",
      "updated_date": "2018-05-02T17:15:40Z",
      "relation_type_id": "discusses"
    }
]

}


*/

CREATE TABLE eventsTable
(
  --UNIQUE event ID. U-N-I-Q-U-E 
  id                         PRIMARY KEY VARCHAR(36) NOT NULL,
  --The URL of the scholarly paper  
  obj_id                     VARCHAR(100) NOT NULL,
  --The id of the CrossRef agent that captured this event
  source_token               VARCHAR(36) NOT NULL,
  --Timestamp of when the event is reported to have occurred
  occurred_at                DATETIME(20) NOT NULL,
  --URL to the status
  subj_id                    VARCHAR(100) NOT NULL,
  --Mitosis steps
  evidence_record            VARCHAR(100) NOT NULL,
  --Original tweet URL if it was retweeted
  originalTweetURL           VARCHAR(100) NOT NULL,
  --Websites name
  source_id                  VARCHAR(20) NOT NULL,
  --Type of mention (Discussion, unveiling, etc)
  relation_type_id           VARCHAR(20) NOT NULL,
);