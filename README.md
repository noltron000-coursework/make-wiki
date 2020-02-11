# :notebook: Personal Wiki
View the [lesson plan] that accompanies this activity.

## Step 1: Follow Setup Guide
> **:star: IMPORTANT**: Change **YOUR_GITHUB_USERNAME** before hitting <kbd>Enter</kbd> on the last step.<br />
**:white_check_mark: EXAMPLE**: Change `git remote add https://github.com/YOUR_GITHUB_USERNAME/makewiki` to `git remote add https://github.com/droxey/makewiki` for [Dani](https://github.com/droxey/makewiki)'s version of the `makewiki` project.
1. **In your browser**, create a **[new public repository](https://github.com/new)** on GitHub called `makewiki`.
1. **In your terminal**, navigate to the directory where you store your projects.
1. **Paste each line below** into the terminal, *one by one*. **Hit <kbd>Enter</kbd> after *each* line**:
	```bash
	git clone https://github.com/make-school-labs/makewiki-v1
	cd makewiki
	git remote remove origin
	git remote add upstream https://github.com/make-school-labs/makewiki-v1
	git remote add origin https://github.com/YOUR_GITHUB_USERNAME/makewiki
	```
1. **Open the `makewiki` repository folder** in your IDE.

## Step 2: CRUD Page Instances (Admin Interface)
1. In your terminal, run `python manage.py runserver`.
2. Visit `http://127.0.0.1:8000/admin/` in your browser.
3. Enter `admin` for the username and `djangopony` for the password.
4. Click `Pages` on the left, underneath `Users` and `Groups`.
5. Add real world data from 5 random Wikipedia articles using http://wikiroulette.co/.

## Step 3: Solve the Challenges
> **NOTE**: Complete the challenges in all files before moving on to stretch challenges. Your grade is dependent on the completion of the challenges only.

1. **REQUIRED**: Complete challenges in each of these files, in order:
	1. `makewiki/urls.py`
	1. `wiki/views.py`
	1. `wiki/urls.py`
	1. `templates/base.html`
	1. You will also need to create templates in `wiki/templates/wiki` for use with your view classes.
1. **OPTIONAL**: Move on to the stretch challenges in the code, or enhance the project using the suggestions below.

> **TIP**: Find all challenges by searching the project for instances of the word `CHALLENGE`. To **search all files in your project directory**, press <kbd>Command</kbd> + <kbd>Shift</kbd> + <kbd>F</kbd>, type `CHALLENGE`, and hit <kbd>Enter</kbd>.

## Step 4: Level Up
### Suggestions
- Create a beautiful user interface for your wiki. [Bootstrap 4](https://getbootstrap.com/docs/4.0/components/) is included with this starter pack! 
- Customize the project and continue to experiment with the codebase.
- Make the models more sophisticated.
- What other features can you dream up? What would look good on your portfolio? Open up a discussion with your instructor to receive personalized feedback.

## Step 5: Add to Portfolio
Add your `makewiki` implementation to your [Make School portfolio](https://www.makeschool.com/portfolio).
