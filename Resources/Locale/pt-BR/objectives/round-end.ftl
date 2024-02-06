objectives-round-end-result =     { $count ->
        [one] Tinha um { $agent }.
       *[other] Tinha { $count } { MAKEPLURAL($agent) }.
    }
objectives-round-end-result-in-custody = { $custody } de { $count } { MAKEPLURAL($agent) } estavam em custódia.
objectives-player-user-named = [color=White]{ $name }[/color] ([color=gray]{ $user }[/color])
objectives-player-user = [color=gray]{ $user }[/color]
objectives-player-named = [color=White]{ $name }[/color]
objectives-no-objectives = { $custody }{ $title } era um { $agent }.
objectives-with-objectives = { $custody }{ $title } era um { $agent } que tinha os seguintes objetivos:
objectives-objective-success = { $objective } | [color={ $markupColor }]Successo![/color]
objectives-objective-fail = { $objective } | [color={ $markupColor }]Falha![/color] ({ $progress }%)
objectives-in-custody = [bold][color=red]| EM CUSTÓDIA | [/color][/bold]
