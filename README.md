# Numpy and Git Warmup!

In this warmup you will practice collaborating
with a partner using github by solving a couple of numpy problems.

Both partners will both get a chance to 
add the other as a collaborator on their fork of this repo,
as well as adding their partner's fork as a remote location
on their local copy.

In a nutshell, you get to play both sides of
the github collaboration process!

## Part 0

1)	Both partners fork this repo to their personal GitHub accounts.
2)	Both partners clone this repo onto their local machine.

	- I suggest you create a subfolder for warmups in your main galvanize directory to clone this repo into.
		Navigate to your galvanize directory and do the following:
		
		```
		mkdir warmups
		cd warmups
		git clone https://github.com/<your github username>/numpy_github_warmup.git
		```

3)	Both partners navigate into their local repo and open vsCode

	```
	cd numpy_github_warmup
	code .
	```

3)	Decide who will be **partner a** and **partner b**
	- **partner a** will be the first to navigate
	- **partner b** will be the first to drive

## Part 1 

1)	**partner a** adds **partner b** as a contributor to their **GitHub** repo
	- This can be done in the settings page under `Manage Access`
	- Don't forget to give them write access!

2)	**partner b** adds **partner a**'s repo as a remote location on their local machine
	- This can be done with the command 
		
		```
		git remote add <name> <url>
		```

	- For example: 

		```
		git remote add zack https://github.com/zackmagnotti/numpy_github_warmup.git
		```

3)	Complete problem 1.1 located in `src/problem1.1.py` with **partner b** driving and **partner a** navigating.
	- **partner b** will need to `add`, `commit`, and `push` the solution to **partner a**'s repo

		```
		git add src/problem1.1.py
		git commit -m 'solutions for problem 1.1'
		git push <name> main
		``` 

	- **partner a** will need to `pull` the solutions from their own repo once **partner b** has pushed them
		
		```bash
		git pull origin main
		# or just
		git pull
		```

4)	Complete problem 1.2 located in `src/problem1.2.py` with the roles reversed.
	- **partner a** will push the solution to their own repo
	- **partner b** will pull the solution from **partner a**'s repo
		```
		git pull <name> main
		```
## Part 2

Complete the steps from part 1 with the roles of **partner a** and **partner b** reversed, solving problems 2.1 and 2.2

- **Partner a** adds **partner b**'s repo as a remote location, and drives first
- **Partner b** adds **partner a** as a contributor on their **GitHub** repo, and navigates first

## Part 3 (optional)

Check out the `git log` after you are finished, and examine the entries. 
Why might keeping track of the commits like this be useful in a large project?
