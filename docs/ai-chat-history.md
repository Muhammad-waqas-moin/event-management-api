tage 10 done

Stage 10 done! 🎉

Ab sab mandatory code aur README GitHub par hain. Ab ek chhota lekin zaroori kaam: AI usage documentation.

Stage 11: AI usage documentation (mandatory)

Assignment mein likha hai ke AI use kiya to yeh 4 cheezein submit karni hain: prompts, chat history, tools aur models, configuration. Is mein imandari zaroori hai: jo AI se banwaya woh likho, aur jo samjha woh bhi.

Step 11.1: Chat history save karo

Yeh sabse zaroori hai, aur abhi kar lo:

Is poori chat ko select karke copy karo, aur docs/ai-chat-history.md mein paste karo, ya
Claude ki settings mein export data ka option ho to use karo, ya chat ka share link bana lo aur AI_USAGE.md mein likh do

Sabse safe: dono karo (file bhi aur link bhi), aur screenshots bhi le sakte ho. Is chat mein koi password ya secret ho to hata dena (humne password kabhi share nahi kiya, to theek hai).

bash
git checkout main
git checkout -b docs/ai-usage
mkdir docs
touch docs/ai-chat-history.md
touch AI_USAGE.md
Step 11.2: AI_USAGE.md banao

Yeh paste karo, aur [ ] wali jagahein apne hisaab se bharo:

markdown

# AI Usage Documentation

## Tools and Models

- **Tool:** Claude (Anthropic) via claude.ai chat interface
- **Model:** [chat ke model selector mein jo naam dikhe, woh yahan likho]
- **Other tools:** None [ya agar koi aur AI tool use kiya ho to likho]

## Configuration

- Web chat with default settings
- No custom system prompt or special configuration
- Language of conversation: Roman Urdu mixed with English
- The AI was used as a **step-by-step teacher/mentor**, not as a one-click code generator

## How AI Was Used

I am a beginner in FastAPI, PostgreSQL and Git, so I used AI to learn and build the project step by step:

1. Understanding the assignment requirements and planning the work in stages
2. Learning concepts: REST API, HTTP methods, status codes, async/await, ORM, dependency injection, Git branching
3. Setting up the environment (Python venv, PostgreSQL, Git, GitHub)
4. Writing and explaining each file: `db.py`, `models.py`, `schemas.py`, `services.py`, `main.py`
5. Debugging errors
   You stopped Claude’s response

stage 10 done

Checking whether the cut-off reply was ever seen.
Stage 10 done, shabash! 🎉

Mera pichla message beech mein kat gaya tha. Is liye Stage 11 ka poora AI_USAGE.md ek jagah de raha hoon. Isay purane wale ki jagah poora replace kar do.

Stage 11: AI usage documentation (mandatory)
Step 11.1: Branch aur files
bash
git checkout main
git checkout -b docs/ai-usage
mkdir docs
touch docs/ai-chat-history.md
touch AI_USAGE.md
Step 11.2: Chat history save karo (abhi)
Is poori chat ko select karke copy karo aur docs/ai-chat-history.md mein paste karo
Agar chat ka share link ban sakta hai to wo bhi AI_USAGE.md mein likh do

Yeh assignment ki requirement hai (“complete chat history”). Aaj ki baaki chat bhi aakhir mein dobara copy karke update kar dena.

Step 11.3: AI_USAGE.md

[ ] wali jagahein apne hisaab se bharo:

markdown

# AI Usage Documentation

## Tools and Models

- **Tool:** Claude (Anthropic), via the claude.ai chat interface
- **Model:** [model selector mein jo naam dikhe woh likho]
- **Other tools:** None [ya jo bhi aur use kiya]

## Configuration

- Web chat with default settings, no custom system prompt
- Conversation language: Roman Urdu mixed with English
- The AI was used as a step-by-step teacher: it explained each concept, then each file in small parts, and I typed and ran the code myself

## How AI Was Used

I am a beginner in FastAPI, PostgreSQL and Git, so I used AI to learn and build the project in stages:

1. Understanding the assignment PDF and splitting the work into two days
2. Learning concepts: REST, HTTP methods, status codes, async/await, ORM, dependency injection, Git branching
3. Environment setup: Python venv, PostgreSQL (Postgres.app), Git and GitHub
4. Writing and explaining each file: `db.py`, `models.py`, `schemas.py`, `services.py`, `main.py`
5. Registration feature and its business rules
6. Debugging errors (for example an import error caused by a missing function in `db.py`)
7. Writing the README

## Prompts Used

Chat ke shuru se apne asli prompts (jo tum ne likhe) yahan list karo. Misaal:

1. Shared the assignment PDF and asked for a beginner-friendly, step-by-step 50% plan, with no topic skipped and the frontend skipped
2. Asked which Python version to use and how a checker would run a local PostgreSQL project
3. Asked for the plan again in smaller beginner-friendly stages with every line explained
4. Asked which code goes into which file
5. Asked how `AsyncSession` gets the session from `db.py`
6. Asked how to test each endpoint in Swagger
7. Asked whether local PostgreSQL or Neon is better for this assignment
8. Asked for the registrations feature (model, schemas, services, endpoints)
9. Error-fixing prompts (venv typo, `get_db` import error, git status questions)

The full list with exact wording is in `docs/ai-chat-history.md`.

## What I Understood and Did Myself

- I typed the code myself file by file, ran every stage and tested every endpoint in Swagger
- I can explain the flow: `main.py` (routes) -> `schemas.py` (validation) -> `services.py` (logic) -> `models.py` -> PostgreSQL
- I fixed my own mistakes, such as a test-file typo and a missing function in `db.py`
- I understand the three business rules and where each is enforced

## Chat History

See `docs/ai-chat-history.md`. [Share link, agar ho: ]

Ek zaroori baat: Is document mein jo likha hai woh sach hona chahiye. “Understood” wali list ko tab hi rakho jab sach mein samajh aaye. Agar koi cheez abhi dhundli hai (jaise Depends, yield, try/except), to mujhse poochho, demo video mein wahi poocha ja sakta hai.

Step 11.4: Commit aur merge
bash
git add AI_USAGE.md docs/
git commit -m "docs: add AI usage documentation"
git push -u origin docs/ai-usage
git checkout main
git merge docs/ai-usage
git push
Ab kya bacha hai
Kaam Status
Event CRUD, registrations, business rules Done
README Done
AI usage doc Stage 11 (abhi)
Swagger screenshots (registrations ke bhi) Check karo
Bonus: pagination + search/filter Agla stage
Bonus: pytest Uske baad
Bonus: JWT Agar waqt bache
Demo video Sabse aakhir, 1.5 ghanta

Aaj 18 Nov hai, deadline EOD. Agar abhi tak kaafi waqt bacha hai to Stage 11 ke baad pagination + search (aasan, 20-30 minute) karte hain.

Jab AI usage doc merge ho jaye to “Stage 11 done” likho. Aur agar waqt kam hai to bata do ke kitne ghante bache hain, main usi hisaab se bonus aur video ka plan bana dunga.

Stage 10 done, shabash! 🎉
Mera pichla message beech mein kat gaya tha. Is liye Stage 11 ka poora AI_USAGE.md ek jagah de raha hoon. Isay purane wale ki jagah poora replace kar do. ye tumnne bola hai but mujy ase smaj nhi ayga . jese hum start se chal rahy hai wese hi chalty hai ab tum mujy stage 11 do

Planning Stage 11 in short pieces.
Stage 11: AI usage documentation (chhote steps mein)

Theek hai, pichli tarah chalte hain: ek ek step, aur har step ka checkpoint.

Yeh stage kyun? Assignment mein likha hai ke AI use kiya to 4 cheezein submit karni hain: prompts, chat history, tools aur models, configuration. Isme sirf sach likhna hai: jo AI se seekha woh bhi, aur jo khud kiya woh bhi.

Is stage mein code nahi hai, sirf do documents banane hain.

Step 11.1: Naya branch aur files
bash
git checkout main
git checkout -b docs/ai-usage
mkdir docs
touch docs/ai-chat-history.md
touch AI_USAGE.md
git checkout main: pehle main par jao
git checkout -b docs/ai-usage: naya branch (documentation ka kaam alag branch par, jaise README ke liye kiya tha)
mkdir docs: docs naam ka folder
touch ...: do khali files

Checkpoint: ls likho. AI_USAGE.md aur docs nazar aane chahiye.

Step 11.2: Chat history save karo

Assignment ko poori chat history chahiye.

Is chat ko upar se neeche tak select karo (ya scroll karke copy karo)
docs/ai-chat-history.md kholo (VS Code mein) aur paste karo
Save karo (Cmd + S)

Agar chat ka share link ban sakta hai (Claude mein chat ke menu mein Share ka option), to wo bhi bana lo. Link Step 11.4 mein kaam aayega.

Aaj ki baqi chat (bonus features, video) bhi aakhir mein dobara copy karke is file mein update karni hogi. Abhi ke liye jitni hai utni save kar lo.

Checkpoint: docs/ai-chat-history.md khali nahi honi chahiye.

Step 11.3: AI_USAGE.md ke sections

Ab AI_USAGE.md kholo. Hum isay 5 chhote tukron mein likhenge. Har tukra file mein neeche add karte jao.

Tukra 1: Title aur Tools
markdown

# AI Usage Documentation

## Tools and Models

- **Tool:** Claude (Anthropic), via the claude.ai chat interface
- **Model:** [chat ke model selector mein jo naam dikhe woh yahan likho]
- **Other tools:** None

# bara heading hai, ## us se chhota

[ ... ] wali jagah apna bharo. Model ka naam chat ke upar ya message box ke paas dikhta hai
Agar kisi aur AI tool (ChatGPT, Copilot wagera) ka bhi istemal kiya ho to “None” ki jagah likho
Tukra 2: Configuration
markdown

## Configuration

- Web chat with default settings, no custom system prompt
- Conversation language: Roman Urdu mixed with English
- The AI was used as a step-by-step teacher. It explained each concept and each file in small parts, and I typed and ran the code myself

Assignment ka “configuration” ka matlab hai AI ki koi khaas settings. Hamari chat default thi, yahi likhna hai.

Tukra 3: AI kaise use hua
markdown

## How AI Was Used

I am a beginner in FastAPI, PostgreSQL and Git, so I used AI to learn and build the project in stages:

1. Understanding the assignment PDF and splitting the work into two days
2. Learning concepts: REST, HTTP methods, status codes, async/await, ORM, dependency injection, Git branching
3. Environment setup: Python venv, PostgreSQL (Postgres.app), Git and GitHub
4. Writing and explaining each file: `db.py`, `models.py`, `schemas.py`, `services.py`, `main.py`
5. Registration feature and its business rules
6. Debugging errors (for example, an import error caused by a missing function in `db.py`)
7. Writing the README

Yeh list bilkul sachi hai, hum ne yahi sab kiya.

Tukra 4: Prompts
markdown

## Prompts Used

1. Shared the assignment PDF and asked for a beginner-friendly, step-by-step plan for half of the assignment, with no topic skipped and the frontend skipped
2. Asked which Python version to use, and how a checker can run a project that uses local PostgreSQL
3. Asked for the plan again in smaller stages with every line of code explained
4. Asked which code goes into which file
5. Asked how `AsyncSession` receives the session from `db.py`
6. Asked how to test every endpoint in Swagger
7. Asked whether local PostgreSQL or Neon is better for this assignment
8. Asked for the registrations feature (model, schemas, services, endpoints)
9. Asked for help with errors (virtual environment typo, `get_db` import error, `git status` output)

The complete list with exact wording is in `docs/ai-chat-history.md`.

Yeh meri taraf se ek khulasa hai. Asli prompts ai-chat-history.md mein hain, jo pehle save ki.

Tukra 5: Maine khud kya kiya
markdown

## What I Did and Understood Myself

- I typed the code file by file, ran every stage, and tested every endpoint in Swagger
- I can explain the flow: `main.py` (routes) -> `schemas.py` (validation) -> `services.py` (logic) -> `models.py` -> PostgreSQL
- I fixed my own mistakes, such as a typo in a test file and a missing function in `db.py`
- I understand the three business rules and where each is enforced

## Chat History

See `docs/ai-chat-history.md`.

Agar share link banaya ho to akhri line mein Link: https://... add kar do.

Ek zaroori baat: Is “understood” wali list ko tab hi rakho jab sach mein samajh aaye. Demo video mein yahi poocha jayega. Agar koi cheez dhundli hai (jaise Depends, yield, try/except), to mujhse poochh lo.

Checkpoint: AI_USAGE.md mein 5 sections hone chahiye: Tools, Configuration, How AI Was Used, Prompts Used, What I Did, aur Chat History.

Step 11.4: Commit aur merge
bash
git add AI_USAGE.md docs/
git commit -m "docs: add AI usage documentation"
git push -u origin docs/ai-usage
git checkout main
git merge docs/ai-usage
git push

Checkpoint: GitHub par main mein AI_USAGE.md aur docs/ folder nazar aaye.

Ab aapka kaam
Step 11.1 se 11.4 karo
Koi error aaye to copy-paste bhej do
Jab merge ho jaye to likho “Stage 11 done”

Phir Stage 12: Pagination (bonus, aasan hai). Agar abhi tak kitne ghante bache hain, bata do to usi hisaab se bonus aur video ka plan bana dunga.
