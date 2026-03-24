Fancy Command Refactoring Kata
==============================

Your colleague has been working on adding custom commands to your fancy program and although they think they are nearly finished, they asked for your help with the unit tests. They have added a new method 'ExecuteFancyCommand' and have found some suitable test data. Unfortunately the code is difficult to test in a unit test since it starts up a graphical UI. (The previous code didn't have any unit tests already since it was written before the coding standards required unit tests.)

Your task is to add unit tests and do any refactoring you feel is needed. In addition, your colleague isn't quite finished with the case when there is more than one custom parameter. If the custom parameters are "//ID: 71mUJgN0sKbr", "//Customer: Acme" then currently the code generates xml that looks like this:


	<Tool id="@NET.Acme.AppFancyCommand">
		<Parameters>
			<Parameter name="CustomParameter" value="//ID: 71mUJgN0sKbr, //Customer: Acme" />
		</Parameters>
	</Tool>

It should instead look like this:

	<Tool id="@NET.Acme.AppFancyCommand">
		<Parameters>
			<Parameter name="CustomParameter" value="//ID: 71mUJgN0sKbr" />
			<Parameter name="CustomParameter" value="//Customer: Acme" />
		</Parameters>
	</Tool>


## Exercise notes
For this exercise a lot of complexity that you would find in real life has been omitted. For example the sample xml given is a tenth of the size of the real xml. The code for the graphical ui is also omitted - it just throws an exception instead of doing that. Use this as an opportunity to practice your testing and refactoring skills.
