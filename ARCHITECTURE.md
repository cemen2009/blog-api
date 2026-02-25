# Architecture of the Blog API

1. [Short Description](#short-description)
1. [Data Types](#data-types)
1. [Main Flow](#flow-diagram)
2. [What flows exist](#what-flows-exist)
3. [Detailed about each flow](#detailed-about-each-flow)

## Short Description

Monolithic shit-plication with low throughput of users. FastAPI backend provides high optimized I/O processes, so ts still can work just fine, thanks to argentinian guy (not german one).
All data stored in one PostgreSQL database for easy development and hard scaling. I will improve it in the future, I promise

## Data Types

You can see descriptive diagram by the link: https://dbdiagram.io/d/blog-api-diagram-699ef792bd82f5fce2cdcdc4

Note: diagram can differ from current implementation due to changing nature of my pet-projects. I can also just forget about this project for half a year

## Main Flow

Here you can see main flow and other type shit: https://excalidraw.com/#json=99oWxVlJSmCNDhiy1K40w,FTJjffAUP5RVwtxDH7S_zw

## What flows exist

* **Account registration**: registration and activation of an user
* **Posting**: existing _(and only activated)_ user can post; content types: text _(250 characters)_, pictures
* **Commenting**: commenting under accessible post
* **Chatting**: people with a subscription _(idk about name: communication/extended/plus)_
can write messages to each other _(because it takes much memory of the database, so it's paid)_
* **Deactivating account**: not removing account but deactivating, can be reactivated during N days; all related to the account data can be saved during N days

## Detailed about each flow

**ACCOUNT REGISTRATION**

1. User send POST request to register and account
2. We created unactivated account and send message on the email of that user to inform 
that he has has N days to activate this account till it will be permanently deleted
3. User activates via activation link account and creates a password or ignores and account will be deleted

---

**POSTING**

1. Activated user sends POST request to create a post with some content (text and/or picture)
2. 