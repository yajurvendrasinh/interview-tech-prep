### Sessions and Authentication

#### User authentication

- There is no single solution for user authentication.

#### Sessions

- Ability to authenticate user without having to ask for username/password every single time they want to do something (i.e. after they've initially logged in)
- If login is correct, backend creates a session ID and hands it back. Everytime the user wants to do something it hands us the session ID and our backend checks to see if the user associated with that session ID can do that action.
- Session IDs are more secure than User IDs in practice. It's nearly impossible to guess a session ID for another user. Accepting User IDs means you could impersonate a user, which is what we do not want.

#### Bcrypt 

Other Hashing algorithms

- MD5
- SHA1

Why Bcrypt?

- MD5 and SHA1 are designed to be fast. Bcrypt is designed to be slow to protect our users.
- Hash the password + the salt to avoid dictionary attacks.
- Dictionary attacks are also hard in bcrypt because bcrypt is very slow.




