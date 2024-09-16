import pytest
from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Triangle import Triangle
from src.Circle import Circle
from src.Square import Square


def test_add_area_valid():
    rect = Rectangle(3, 4)
    circle = Circle(4)
    tr = Triangle(3, 4, 5)
    sq = Square(7)
    assert rect.add_area(circle) == rect.get_area + circle.get_area
    assert rect.add_area(tr) == rect.get_area + tr.get_area
    assert rect.add_area(sq) == rect.get_area + sq.get_area

    assert circle.add_area(tr) == circle.get_area + tr.get_area
    assert circle.add_area(sq) == circle.get_area + sq.get_area

    assert tr.add_area(sq) == tr.get_area + sq.get_area


@pytest.mark.parametrize(
    "not_figure",
    [3, "test", 2.4],
    ids=["integer", "string", "float"]
)
def test_add_area_invalid(not_figure):
    rect = Rectangle(3, 4)
    with pytest.raises(ValueError, match=f"{not_figure} not a Figure object"):
        rect.add_area(not_figure)
