# -*- coding: utf-8 -*-

import pytest
import pytamil.தமிழ்
from pytamil.தமிழ் import புணர்ச்சி

@pytest.mark.parametrize("நிலைமொழி,வருமொழி,தொடர்மொழி", \
						[ 
							('சே','அடி',['சேயடி','சேவடி']) 
						])
def test_தொடர்மொழி_ஆக்கு(நிலைமொழி, வருமொழி , தொடர்மொழி):
	தொடர்மொழி_பதங்கள் = புணர்ச்சி.தொடர்மொழி_ஆக்கு(நிலைமொழி, வருமொழி )
	assert len(தொடர்மொழி_பதங்கள்) == len(தொடர்மொழி)

	for பதம் in தொடர்மொழி_பதங்கள்:
		assert பதம் in தொடர்மொழி


def test_file1_method2():
	x=5
	y=6
	assert x+1 == y,"test failed" 