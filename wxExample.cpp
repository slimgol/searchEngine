/**********************************************
 *  Step 1: Always include the header file wx.h					    
 **********************************************/
#include <wx/wx.h>


/**********************************************
 *  Step 2: Name an inherited application class
 *          from wxApp and declare it with the
 *          function to execute the program
 **********************************************/
class MyApp: public wxApp
    {
        virtual bool OnInit();
    };



/**********************************************
 *   Step 3: Declare the inherited main frame
 *           class from wxFrame. In this class
 *	         also will ALL the events handlers
 *           be declared
 **********************************************/
class MyFrame: public wxFrame
{
    private:
        DECLARE_EVENT_TABLE() //To declare events items
    
    public:
        MyFrame(const wxString& title, const wxPoint& pos, 
                const wxSize& size);
        
        void OnQuit(wxCommandEvent& event);   // Quit function
        void OnAbout(wxCommandEvent& event);  // About function
        void OnHelp(wxCommandEvent& event);   // Help function
    };



/**********************************************
 *  Step 4. Declare the compiler directives
 ***********************************************/
DECLARE_APP(MyApp)		// Declare Application class
IMPLEMENT_APP(MyApp)	// Create Application class object


enum
        {
            ID_Quit = wxID_HIGHEST + 1,
            ID_About,
            ID_Help,
        };

BEGIN_EVENT_TABLE ( MyFrame, wxFrame )
        EVT_MENU ( ID_Quit, MyFrame::OnQuit )
        EVT_MENU ( ID_About, MyFrame::OnAbout )
        EVT_MENU ( ID_Help, MyFrame::OnHelp )
END_EVENT_TABLE () 



/**********************************************
 *  Step 5. Define the Application class function
 *          to initialize the application
 ***********************************************/
bool MyApp::OnInit()
    {
        // Create the main application window
        MyFrame *frame = new MyFrame(
                                wxT("Minimal wxWidgets App"),
                                wxPoint(50,50),
                                wxSize(500,400) );
    
        // Display the window
        frame->Show(TRUE);
    
        SetTopWindow(frame);
    
        return TRUE;
    
    }


/**********************************************
 *  Step 6:  Define the Constructor functions
 *           for the Frame class
 **********************************************/
MyFrame::MyFrame ( const wxString& title,
                   const wxPoint& pos,
                   const wxSize& size) :
                   wxFrame(( wxFrame *)NULL, -1,
                             title, pos, size)
    {
        // Set the frame icon - optional
        SetIcon(wxIcon(wxT("uwiIcon.xpm")));
    
        // Create a "File" main-menu item
        wxMenu *menuFile = new wxMenu;
    
        // Append menu items (About and Exit) to the
        // "File" menu item
        menuFile->Append( ID_About, wxT("&About...") );
        menuFile->AppendSeparator();
        menuFile->Append( ID_Quit, wxT("E&xit") );
    
        //Create a "Help" main-menu item
        wxMenu *menuHelp = new wxMenu;
    
        //Append "Help" sub-menu item to it 
        menuHelp->Append(ID_Help, wxT("&Help..."));
    
        //Append "About" sub-menu item to it 
        menuHelp->Append(ID_About, wxT("&About"));
    
        //Create a Main menu bar
        wxMenuBar *menuBar = new wxMenuBar;
    
        //Append the main menu items ("File" and "Help") to it
        menuBar->Append( menuFile, wxT("&File") );
        menuBar->Append( menuHelp, wxT("&Help") );
    
        // ... and now... attach this main menu bar to the frame
        SetMenuBar( menuBar );
    
        // Create a status bar just for fun
        CreateStatusBar(2);
    
        //Put something in the first section of the status bar
        SetStatusText( wxT("Welcome to wxWidgets!") );
    
        //Put something in the second section of the status bar
        SetStatusText( wxT("COMP2611 - Data Structures"), 1 );
    
    }


/**********************************************
 *  Step 7:  Define member functions for the
 *           Frame class
 **********************************************/
void MyFrame::OnQuit(wxCommandEvent& WXUNUSED(event))
    {
        Close ( TRUE );
    }



void MyFrame::OnAbout ( wxCommandEvent& WXUNUSED ( event ) )
    {
        wxString msg;
    
        msg.Printf(wxT("Hello and welcome to %s"), wxVERSION_STRING);
    
        wxMessageBox(msg, wxT("About Minimal"), wxOK | wxICON_INFORMATION, this);
    }


void MyFrame::OnHelp ( wxCommandEvent& WXUNUSED ( event ) )
    {
        wxMessageBox(wxT("HELP!!!"), wxT("Minimal Help"), 
                     wxOK | wxCANCEL | wxICON_QUESTION, this);
    }

