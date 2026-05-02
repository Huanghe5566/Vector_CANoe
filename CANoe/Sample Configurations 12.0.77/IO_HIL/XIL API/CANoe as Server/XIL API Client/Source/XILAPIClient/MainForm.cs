// Created by Brock, Boris (visbbr), 2015-02-23
// Copyright (c) Vector Informatik GmbH. All rights reserved.

#region Usings

using System;
using System.Windows.Forms;

#endregion

namespace XILAPIClient
{
  public partial class MainForm : Form
  {
    #region Configuration Strings

    private const string ConfigVendorName = "Vector";

    private const string ConfigProductName = "CANoe";

    private const string ConfigProductVersion = "8.5";

    private const string ConfigMAPortConfig = "../../../XIL API Configuration/VectorMAPortConfig.xml";

    private const string ConfigVariableName = "Test::Variable1";

    #endregion


    #region Members

    private readonly XILAPIWrapper mXil;

    #endregion


    #region Methods

    /// <summary>
    ///   Initializes a new instance of the <see cref="MainForm" /> class.
    /// </summary>
    public MainForm()
    {
      InitializeComponent();
      mXil = new XILAPIWrapper();
    }

    /// <summary>
    /// Called when [load].
    /// </summary>
    /// <param name="sender">The sender.</param>
    /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
    private void OnLoad(object sender, EventArgs e)
    {
      // Initialize combo boxes
      cbxVendor.SelectedIndex = 0;
      cbxProduct.SelectedIndex = 0;
      cbxProductVersion.SelectedIndex = 0;
    }

    /// <summary>
    ///   Connects to CANoe
    /// </summary>
    /// <param name="sender">The sender.</param>
    /// <param name="e">The <see cref="EventArgs" /> instance containing the event data.</param>
    private void OnBtnConnectClick(object sender, EventArgs e)
    {
      try
      {
        mXil.Init(cbxVendor.SelectedItem.ToString(), cbxProduct.SelectedItem.ToString(), cbxProductVersion.SelectedItem.ToString(), ConfigMAPortConfig);
        mTimer.Enabled = true;
        mBtnConnect.Enabled = false;
        mBtnDisconnect.Enabled = true;
      }
      catch (Exception ex)
      {
        MessageBox.Show(ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
      }
    }

    /// <summary>
    ///   Called when [form closing].
    /// </summary>
    /// <param name="sender">The sender.</param>
    /// <param name="e">The <see cref="FormClosingEventArgs" /> instance containing the event data.</param>
    private void OnFormClosing(object sender, FormClosingEventArgs e)
    {
      if (mXil.IsConnected)
        mXil.Shutdown();
    }

    /// <summary>
    ///   Disconnects from CANoe
    /// </summary>
    /// <param name="sender">The sender.</param>
    /// <param name="e">The <see cref="EventArgs" /> instance containing the event data.</param>
    private void OnMBtnDisconnectClick(object sender, EventArgs e)
    {
      mXil.Shutdown();
      mTimer.Enabled = false;
      mBtnConnect.Enabled = true;
      mBtnDisconnect.Enabled = false;
    }

    /// <summary>
    ///   Updates the GUI with current variable values
    /// </summary>
    /// <param name="sender">The sender.</param>
    /// <param name="e">The <see cref="EventArgs" /> instance containing the event data.</param>
    private void OnTimerTick(object sender, EventArgs e)
    {
      var curvalue = mXil.ReadVariable(ConfigVariableName);

      mNumCurValue.Value = (decimal) Math.Round(curvalue, 2);
      mBarCurValue.Value = (int) curvalue;
    }

    /// <summary>
    /// Called when the Quit button is pressed
    /// </summary>
    /// <param name="sender">The sender.</param>
    /// <param name="e">The <see cref="EventArgs"/> instance containing the event data.</param>
    private void OnBtnQuitClick(object sender, EventArgs e)
    {
      this.Close();
    }

    #endregion
  }
}