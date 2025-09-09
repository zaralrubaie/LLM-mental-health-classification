import pytest
from mental_health.data_processing import assign_label

def test_assign_label_depression():
    assert assign_label("I feel very sad and worthless") == "depression"

def test_assign_label_anxiety():
    assert assign_label("My stress levels are very high") == "anxiety"

def test_assign_label_normal():
    assert assign_label("I went for a walk and felt fine") == "normal"
