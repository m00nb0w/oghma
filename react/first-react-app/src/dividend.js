import React, { Component } from 'react';
import DividendRow from './DividendRow';

class Dividend extends Component {
  constructor(props){
    super(props);
    this.state = {
      lists: [
        {
          name: 'TCS',
          dividendYield: '0.4'
        },
        {
          name: 'Infosys',
          dividendYield: '0.5'
        },
        {
          name: 'HCL',
          dividendYield: '0.6'
        }]
    }
  }
  render() {
    return (
      <table>
        <thead>
            <tr>
            <td>Name</td>
            <td>DividendYield</td>
            </tr>
        </thead>
        <tbody>
          {this.state.lists.map(list => {
            return <DividendRow name={list.name} dividendYield={list.dividendYield} />
          })}
        </tbody>
      </table>
    );
  }
}

export default Dividend;
