zsh-battery-state
=================
zsh-battery-state is a plugin to display the state of battery in zsh.


<storng><h3>1.Install oh-my-zsh</h3></storng> 

Follow the guide here:https://github.com/robbyrussell/oh-my-zsh

<storng><h3>2.Clone zsh_battery_state from GitCafé</h3></storng>

<h4>git clone git@gitcafe.com:Jactry/zsh_battery_state.git ~/.oh-my-zsh/plugins/zsh-battery-state</h4>

<storng><h3>3.Set zsh to support it</h3></storng>

Add this to your ~/.zshrc :

<code>function battery {
    </p>BATSTATE=~/.oh-my-zsh/plugins/zsh-battery-state/battery_state.py</h4>
    </p>echo `$BATSTATE` 2>/dev/null
</p>}

</p>RPROMPT='$(battery)'</code>

<h2>Note:</h2>If does not work in your zsh,please check your .zshrc and make sure it include this:
</p>
<code>ZSH=$HOME/.oh-my-zsh
</p>source $ZSH/oh-my-zsh.sh</code>

 
<h4>Enjoy it!</p>And if you meet some problem when you use it please contact me.</p>My EMail is jactry92@gmail.com Thank you!</h4>

