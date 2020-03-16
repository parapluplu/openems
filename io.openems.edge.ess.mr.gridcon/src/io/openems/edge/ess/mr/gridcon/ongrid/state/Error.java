package io.openems.edge.ess.mr.gridcon.ongrid.state;

import io.openems.common.exceptions.OpenemsError.OpenemsNamedException;
import io.openems.edge.ess.mr.gridcon.IState;
import io.openems.edge.ess.mr.gridcon.ongrid.OnGridState;

public class Error extends BasteState {

	@Override
	public IState getState() {
		return OnGridState.ERROR;
	}

	@Override
	public IState getNextState() {
		return OnGridState.ONGRID; //Currently it is ot defined, so it is always ongrid
	}
	
	@Override
	public void act() throws OpenemsNamedException {
		// Nothing to do		
	}
}
