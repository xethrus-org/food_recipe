from flask import Blueprint, render_template, redirect, url_for
from .forms import RecipeForm
from .models import Recipe
from . import db

bp = Blueprint("main", __name__)

#simple route for creating and pushing a new recipe to db
@bp.route("/recipe/new", methods=["GET", "POST"])
def create_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(
            title=form.title.data,
            description=form.description.data,
            ingredients=form.ingredients.data,
            instructions=form.instructions.data,
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("main.display_recipes"))
    else:
        print("form error:", form.errors)
    return render_template("new_recipe.html", form=form)

#simple route for finding the info on a specific recipe based on its auto-incrementing id
@bp.route("/recipe/<int:id>", methods=["GET"])
def get_recipe(id):
    requested_recipe = Recipe.query.get_or_404(id)
    return render_template("recipe_detail.html", recipe=requested_recipe)


@bp.route("/recipe/<int:id>/delete", methods=["GET", "POST"])
def delete_recipe(id):
    recipe_to_delete = Recipe.query.get_or_404(id)
    db.session.delete(recipe_to_delete)
    db.session.commit()
    return redirect(url_for("main.display_recipes"))


@bp.route("/recipes", methods=["GET"])
def display_recipes():
    recipes_to_display = Recipe.query.all()
    return render_template("index.html", recipes=recipes_to_display)
