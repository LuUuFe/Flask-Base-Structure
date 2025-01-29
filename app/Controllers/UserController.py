from flask import render_template, redirect, url_for, flash
from app import db
from app.Models.User import User
from app.Forms.UserForm import UserForm


def index():
    """
    Renders the user registration form and displays all registered users in a table.

    :return: A rendered template with the registration form and all users
    """

    # Get all users from the database
    users = User.query.all()

    # Render the user.html template with the registration form and all users
    return render_template("pages/user/index.html", users=users)


def create():
    """
    Handles the user registration form and adds a new user to the database.

    If the form is valid, it creates a new User object and adds it to the database.
    After successful registration, it flashes a success message and redirects to this route.

    Otherwise, it renders the create.html template with the registration form and all users.
    """

    # Create a form object for the user registration form
    form = UserForm()

    if form.validate_on_submit():
        # Create a dictionary with the form data
        userData = {
            "name": form.name.data,
            "email": form.email.data,
        }

        # Create a new User object and add it to the database
        newUser = User(**userData)
        db.session.add(newUser)
        db.session.commit()

        # Flash a success message and redirect to this route
        flash("User registered successfully!", "success")
        return redirect(url_for("main.user"))

    # Render the create.html template with the registration form, but do not store it in the browsing history
    return render_template("pages/user/create.html", form=form)


def edit(id: int):
    """
    Handles the user edit form and updates a user in the database.

    If the form is valid, it updates the user object and commits the changes to the database.
    After successful update, it flashes a success message and redirects to the user list page.

    Otherwise, it renders the user.html template with the edit form and all users.
    """

    # Retrieve the user object from the database or return a 404 error if not found
    user = User.query.get_or_404(id)

    # Instantiate the form with the user object
    form = UserForm(obj=user)

    if form.validate_on_submit():
        # Update the user object with the form data
        user.name = form.name.data
        user.email = form.email.data

        # Commit the changes to the database
        db.session.commit()

        # Flash a success message and redirect to the user list page
        flash(f"User {user.name} updated successfully!", "success")
        return redirect(url_for("main.user"))

    # Render the edit template with the form and user data
    return render_template("pages/user/edit.html", form=form, user=user)


def destroy(id: int):
    """
    Deletes a user from the database.

    Retrieves the user object from the database or returns a 404 error if not found.
    Deletes the user object from the database and commits the changes.
    Flashes a success message with the user's name and redirects to the user list page.

    :param id: The ID of the user to delete
    :return: A redirect to the user list page
    """
    # Retrieve the user object from the database or return a 404 error if not found
    user = User.query.get_or_404(id)

    # Delete the user object from the database and commit the changes
    db.session.delete(user)
    db.session.commit()

    # Flash a success message with the user's name and redirect to the user list page
    flash(f"User {user.name} deleted successfully!", "success")
    return redirect(url_for("main.user"))
