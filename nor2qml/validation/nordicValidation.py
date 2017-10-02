import sys
import os
import logging

from nor2qml.validation import nordicMainValidation
from nor2qml.validation import nordicMacroseismicValidation
from nor2qml.validation import nordicErrorValidation
from nor2qml.validation import nordicCommentValidation
from nor2qml.validation import nordicWaveformValidation
from nor2qml.validation import nordicPhaseDataValidation

eventTypeValues = {"O":1, "A":2, "P":3, "R":4, "F":5, "S":6}
def validateNordic(nordic_event):
	validation_error = False

	if nordic_event.headers[0].tpe != 1:
		msg = "Validation Error - Nordic Event: First Header is not of type 1! {0}"
		logging.error(msg.format(nordic_event.headers[0].tpe))
		validation_error = True

	for header in nordic_event.headers:
		if (header.tpe == 1):
			if not nordicMainValidation.validateMainHeader(header):
				validation_error = True
		elif (header.tpe == 2):
			if not nordicMacroseismicValidation.validateMacroseismicHeader(header):
				validation_error = True
		elif (header.tpe == 3):
			if not nordicCommentValidation.validateCommentHeader(header):
				validation_error = True
		elif (header.tpe == 5):
			if not nordicErrorValidation.validateErrorHeader(header):
				validation_error = True
		elif (header.tpe == 6):
			if not nordicWaveformValidation.validateWaveformHeader(header):
				validation_error = True

	for phase_data in nordic_event.data:
		if not nordicPhaseDataValidation.validatePhaseData(phase_data):
			validation_error = True

	return not validation_error
