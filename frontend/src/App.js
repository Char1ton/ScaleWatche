import React, { Component } from "react";
import Modal from "./components/Modal"
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      scalewatch: [],
      modal: false,
	activeItem:{title:"",
	description:"",
	line:"",
	},
    };
  }

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("/api/ScaleWatcher/")
      .then((res) => this.setState({ scalewatch: res.data }))
      .catch((err) => console.log(err));
};

toggle = () => {
    this.setState({ modal: !this.state.modal });
  };

handleSubmit = (item) => {
    this.toggle();

    if (item.id) {
      axios
        .put(`/api/ScaleWatcher/${item.id}/`, item)
        .then((res) => this.refreshList());
      return;
    }
    axios
      .post("/api/ScaleWatcher/", item)
      .then((res) => this.refreshList());
  };


editItem = (item) => {
    this.setState({ activeItem: item, modal: !this.state.modal });
  };

renderItems = () => {
    const { viewCompleted } = this.state;
    const newItems = this.state.scalewatch.filter(
      (item) => item.completed == viewCompleted
    );

    return newItems.map((item) => (
	<li
        key={item.line}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span>
          {item.title}
        </span>
	<span>
	   {item.description}
	</span>
	<span>
          <button
	    color="red"
	    appearance="primary"
	    onClick={()=>this.editItem(item)}	    
          >
            Report Problem
	    
          </button>
	</span>
	</li>
   
    ));
  };
  render() {
    return (
      <main className="container">
        <h1 className="text-black text-uppercase text-center my-4">Scale Watcher</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul>
		</div>
          </div>
        </div>
	{this.state.modal ? (
          <Modal
            activeItem={this.state.activeItem}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}
      </main>
    );
  }
}

export default App;