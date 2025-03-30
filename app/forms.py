from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class RecipeForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=80)])
    description = TextAreaField("Description", validators=[DataRequired()])
    ingredients = TextAreaField("Ingredients", validators=[DataRequired()])
    instructions = TextAreaField("Instructions", validators=[DataRequired()])
    instructions = TextAreaField("time required", validators=[DataRequired()])
    submit = SubmitField("Submit")

