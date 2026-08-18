# Example: rewriting a procedure

A realistic before-and-after. The point isn't that the "after" is prettier — it's
that each change maps to a specific rule, and a reviewer can defend every one.

## Before

> ## Setting Up Your New Deployment Pipeline
>
> In this section, we will walk you through how to easily set up the deployment
> pipeline. Note that the pipeline is currently only supported on Linux.
>
> To set up the pipeline:
>
> 1. Run the following command to install the CLI:
>    ```
>    $ npm install -g deploy-cli
>    ```
> 2. Simply login using your API key. Your key can be found in the settings page
>    (see the screenshot below).
> 3. Press Ctrl+Shift+P and type "init", then hit enter. The init dialog will be
>    displayed.
> 4. In the dialog below, click the Create New Pipeline button in the bottom right,
>    and the pipeline will then be created for you.
> 5. (Optional) Whitelist your CI runner's IP.
> 6. The master branch will be deployed automatically once the pipeline is created.
>    If you desire a different branch, you may change it in settings, though we will
>    be adding better support for this soon.

## After

> ## Set up a deployment pipeline
>
> This pipeline runs on Linux only.
>
> Before you start, get your API key from the **Settings** page.
>
> To set up the pipeline, follow these steps:
>
> 1. Install the CLI:
>    ```
>    npm install -g deploy-cli
>    ```
> 2. Sign in with your API key:
>    ```
>    deploy-cli auth login --key API_KEY
>    ```
>    Replace `API_KEY` with the key from the **Settings** page.
> 3. In the command palette, enter `init`, and then press **Enter**. The **Initialize
>    pipeline** dialog opens.
> 4. In the **Initialize pipeline** dialog, click **Create pipeline**.
> 5. Optional: To let your CI runner reach the service, add its IP address to the
>    allowlist.
>
> After the pipeline is created, it deploys the `main` branch. To deploy a different
> branch, change the branch on the **Settings** page.

## What changed, and why

| Change | Rule |
| --- | --- |
| "Setting Up Your New Deployment Pipeline" → "Set up a deployment pipeline" | Sentence case; dropped *New* as a dating word |
| "we will walk you through" → deleted | Second person, not first; the intro repeated the heading |
| "easily" and "Simply" → deleted | *easy* and *simply* belittle a stuck reader |
| "is currently only supported" → "runs on Linux only" | *currently* is implied; *only* moved next to what it modifies |
| Prerequisite (API key) moved above step 1 | Readers need what they need before they start |
| "Run the following command to install" → "Install the CLI:" | Focus on what the command does, not that it's a command |
| `$` prompt removed | Prompts break copy-paste |
| "login" → "Sign in" | *login* is the noun; *sign in* is the preferred verb |
| Added the actual command and a placeholder explanation | Steps show the command, then explain placeholders in order |
| "Ctrl+Shift+P" → "In the command palette" | Don't make a keyboard shortcut the only path |
| "hit enter" → "press **Enter**" | *hit* isn't a verb for keys; UI elements in bold; Enter belongs in the same step |
| "the init dialog will be displayed" → "the **Initialize pipeline** dialog opens" | Present tense; *display* is transitive; name the element by its label |
| "In the dialog below" → named the dialog | No directional language |
| "Create New Pipeline" → "Create pipeline" | Avoid *Create a new …*; match the real label |
| "in the bottom right" → deleted | Refer to elements by label, not position |
| "the pipeline will then be created for you" → moved to a result sentence | Active voice, present tense, no passive filler |
| "(Optional)" → "Optional:" | The guide's form for optional steps |
| "Whitelist your IP" → "add its IP address to the allowlist" | *whitelist* isn't used, and the replacement isn't used as a verb either |
| "master branch" → `main` branch | Non-inclusive term; branch name in code font |
| "If you desire" → "To deploy a different branch" | *desire* → *want*, and the goal comes before the action |
| "you may change it" → "change the branch" | *may* is reserved for policy; *can* or an imperative is clearer |
| "we will be adding better support soon" → deleted | Don't pre-announce; *soon* dates the doc |
| Result moved out of the numbered list | A consequence of finishing isn't a step |

Note the step count dropped from six to five while the doc got *more* informative —
the deletions were filler, and the additions were the command and the placeholder
that the reader actually needed.

---

*Provenance: rules cited above come from the Google developer documentation style
guide (CC BY 4.0). The before/after text is original, written for this skill.
Canonical source: https://developers.google.com/style*
