# GG Backend
An API Backend for the GG Tools / Apps

## How?
The Database stores 2 Tables for Surveys. One Table stores Survey 'Blueprints' which describe the questions, name etc. for a survey. The other Table stores all responses / completed surveys from the users. These Responses have a ID, a USER ID and SURVEY ID. The answers and the blueprints of the questions are stored via Postgres JSONField.
### Questions Blueprint:
As described the questions are saved / configured via json. A list of all possible settings will soon be added and a web interface for admins soon after. 
#### Example
```json
[
  ...questions...
    {
        question: "What is your name?",
        description: "we need your name to veryify you",
        type: "text",
        required: True,
        result_type: string
    },
  ...questions...
]
```
optionally 'optiosn' can be added for mulitplse choice questions or a set of responses.
```json
        options: [
            { name: "John", value: int },
            { name: "Lisa", value: int },
            { name: "Other" value string }
        ],
```


