.PHONY:	run

run:	gator_taxi.py
	python3 $< $(word 2,$(MAKECMDGOALS))

%:
	@:
