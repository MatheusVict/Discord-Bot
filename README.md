# Project Setup

Follow the steps below to set up the project on your enviroment.

## Local Development

Create a virtual enviroment with Python 3.7 or higher.

Install required packges:

```
pip3 install -r requirements.txt
```

# Usage

**OBS:** First, you need to create a new file called```.env```, and then put your bot token inside it, similar to ```.env.example``` 

### File: ```01_on_message.py```

**Reply only to messages that start with "$hello" or "hello there"  and set an emoji for it.**

![Screenshot from 2023-06-16 13-16-06](https://github.com/MatheusVict/PataAmigaAPI/assets/103688000/cce2f3d1-052c-48f8-a0aa-358229135c2c)

### File: ```02_reactions_and_edits.py```

**Listen to message edits and display who edited it, before and after.**

![image](https://github.com/MatheusVict/PataAmigaAPI/assets/103688000/643d00d2-647a-4895-8f58-6940373c8967)

**Show who reacted and the emoji that was used.**

![image](https://github.com/MatheusVict/PataAmigaAPI/assets/103688000/6bac49e0-cec0-41f8-b1cc-8fe626725a7f)

### File: ```03_reaction_.roles.py```

**Listen to a message and assign a role to anyone who uses any emoji on that specific message.**

![image](https://github.com/MatheusVict/PataAmigaAPI/assets/103688000/ab3c3296-9aed-4231-beb1-c93b5a33ef52)

![image](https://github.com/MatheusVict/PataAmigaAPI/assets/103688000/608c9b4b-81b7-40f9-91bb-6105d9b0afda)

**When you remove the emoji it remove your role**
**you set the message's id here:**
```
class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
      
        super().__init__(*args, **kwargs)
        self.target_message_id = idMessage <----
```

### File: ```04_commands.roles.py```

**Custom commands with the prefix "!" - Use "!help" to see all commands with examples.**

![image](https://github.com/MatheusVict/PataAmigaAPI/assets/103688000/dbf53eec-fe32-4cc0-a3a2-dfa56d26ba0c)

### File: ```05_help_add_embeds.roles.py```

**Custom commands with the prefix "!" and a custom help message.**

![image](https://github.com/MatheusVict/PataAmigaAPI/assets/103688000/e447ce44-5b5e-433f-8696-40dd4c943b61)
